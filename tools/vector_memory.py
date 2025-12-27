#!/usr/bin/env python3
"""
Vector Memory System for Claude Code
Uses ChromaDB for semantic search and knowledge storage
"""

import sys
import json
from datetime import datetime
from pathlib import Path

try:
    import chromadb
    from chromadb.config import Settings
except ImportError:
    print("ChromaDB not installed. Run: pip install chromadb sentence-transformers")
    sys.exit(1)


class VectorMemory:
    def __init__(self, db_path=None):
        if db_path is None:
            db_path = Path.home() / ".claude" / "memory" / "vector_db"

        db_path.mkdir(parents=True, exist_ok=True)

        self.client = chromadb.PersistentClient(path=str(db_path))
        self.collection = self.client.get_or_create_collection(
            name="claude_memory",
            metadata={"hnsw:space": "cosine"}
        )

    def save(self, content: str, content_type: str = "general", metadata: dict = None):
        """Save content to memory"""
        if metadata is None:
            metadata = {}

        metadata.update({
            "type": content_type,
            "timestamp": datetime.now().isoformat()
        })

        doc_id = f"{content_type}_{datetime.now().timestamp()}"

        self.collection.add(
            documents=[content],
            metadatas=[metadata],
            ids=[doc_id]
        )

        print(f"✓ Saved to memory: {content_type}")
        return doc_id

    def search(self, query: str, content_type: str = None, limit: int = 5):
        """Search memory"""
        where = {"type": content_type} if content_type else None

        results = self.collection.query(
            query_texts=[query],
            n_results=limit,
            where=where
        )

        if not results['documents'][0]:
            print("No results found")
            return []

        formatted_results = []
        for i, doc in enumerate(results['documents'][0]):
            metadata = results['metadatas'][0][i]
            distance = results['distances'][0][i] if 'distances' in results else 0

            formatted_results.append({
                "content": doc,
                "type": metadata.get("type", "unknown"),
                "timestamp": metadata.get("timestamp", "unknown"),
                "score": 1 - distance
            })

        return formatted_results

    def stats(self):
        """Get memory statistics"""
        count = self.collection.count()

        # Get all metadata to count by type
        all_items = self.collection.get()
        types = {}
        for metadata in all_items['metadatas']:
            t = metadata.get('type', 'unknown')
            types[t] = types.get(t, 0) + 1

        return {
            "total_entries": count,
            "by_type": types
        }


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python vector_memory.py save <content> [type]")
        print("  python vector_memory.py search <query> [type]")
        print("  python vector_memory.py stats")
        sys.exit(1)

    memory = VectorMemory()
    command = sys.argv[1]

    if command == "save":
        if len(sys.argv) < 3:
            print("Error: content required")
            sys.exit(1)

        content = sys.argv[2]
        content_type = sys.argv[3] if len(sys.argv) > 3 else "general"

        memory.save(content, content_type)

    elif command == "search":
        if len(sys.argv) < 3:
            print("Error: query required")
            sys.exit(1)

        query = sys.argv[2]
        content_type = sys.argv[3] if len(sys.argv) > 3 else None

        results = memory.search(query, content_type)

        print(f"\nFound {len(results)} results:\n")
        for i, result in enumerate(results, 1):
            print(f"{i}. [{result['type']}] Score: {result['score']:.2f}")
            print(f"   {result['content'][:200]}...")
            print(f"   Time: {result['timestamp']}\n")

    elif command == "stats":
        stats = memory.stats()
        print(json.dumps(stats, indent=2))

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
