"""Simple Command Line Interface for AI Bot.

Use this if you prefer command-line over GUI.
"""
from ai_bot.core.ai_engine import AIEngine
from ai_bot.modules.web_search import WebSearcher
from ai_bot.modules.wikipedia_offline import WikipediaOffline
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class AIBOT_CLI:
    """Command line interface for AI Bot."""

    def __init__(self):
        """Initialize the CLI with AI engine and search modules."""
        self.engine = AIEngine()
        self.web_searcher = WebSearcher()
        self.wiki_offline = WikipediaOffline()

        # Initialize Wikipedia
        if not self.wiki_offline.initialized:
            self.wiki_offline.setup_database()

    def print_header(self):
        """Print welcome header."""
        print("\n" + "="*60)
        print("🤖 AI BOT - Hybrid Search Engine (CLI Version)")
        print("="*60)
        print("Search online and offline from your terminal!\n")

    def print_menu(self):
        """Print available commands."""
        print("\nAvailable Commands:")
        print("  search <query>  - Search for something")
        print("  mode <m>        - Change mode (hybrid/online/offline)")
        print("  history         - Show search history")
        print("  offline-list    - List available offline articles")
        print("  clear           - Clear cache")
        print("  help            - Show this menu")
        print("  quit/exit       - Exit the application\n")

    def search(self, query: str) -> None:
        """Perform a search.

        Args:
            query: The search query string.
        """
        if not query:
            print("❌ Empty search query")
            return

        print(f"\n🔍 Searching for: {query}")
        print("Please wait...\n")

        result = self.engine.process_query(
            query,
            self.web_searcher.search,
            self.wiki_offline.search
        )

        if result['success']:
            print("✅ Search successful!\n")
            print("-" * 60)
            print(result['response'])
            print("-" * 60)
            print(f"\nMode: {result['mode']}")
            print(f"Sources: {', '.join(result['sources'])}")
            print(f"Time: {result['timestamp']}")
        else:
            error_msg = result.get('response', 'Unknown error')
            print(f"❌ Search failed: {error_msg}")

    def change_mode(self, mode: str) -> None:
        """Change search mode.

        Args:
            mode: The mode to switch to (hybrid, online, or offline).
        """
        if self.engine.set_mode(mode):
            print(f"✅ Mode changed to: {mode}")
        else:
            print("❌ Invalid mode. Use: hybrid, online, or offline")

    def show_history(self, limit: int = 10) -> None:
        """Show search history.

        Args:
            limit: Maximum number of history items to display.
        """
        history = self.engine.get_history(limit)

        if not history:
            print("No search history")
            return

        print(f"\n📜 Last {len(history)} searches:\n")
        for i, item in enumerate(history, 1):
            query = item.get('query', 'N/A')
            mode = item.get('mode', 'N/A')
            timestamp = item.get('timestamp', 'N/A')[:16]
            print(f"  {i}. [{timestamp}] ({mode}) {query}")

    def list_offline_articles(self) -> None:
        """List available offline articles."""
        articles = self.wiki_offline.list_articles(20)
        count = self.wiki_offline.get_article_count()

        print("\n📚 Wikipedia Offline Database")
        print(f"   Total articles: {count}\n")

        if articles:
            print("Available articles:")
            for i, article in enumerate(articles, 1):
                print(f"  {i}. {article}")
        else:
            print("No articles found in database")

    def run(self) -> None:
        """Main CLI loop."""
        self.print_header()
        self.print_menu()

        while True:
            try:
                command = input("ai-bot> ").strip()

                if not command:
                    continue

                parts = command.split(None, 1)
                cmd = parts[0].lower()
                arg = parts[1] if len(parts) > 1 else ""

                if cmd in ['quit', 'exit', 'q']:
                    print("\n👋 Goodbye!")
                    break

                elif cmd == 'search':
                    if arg:
                        self.search(arg)
                    else:
                        print("Usage: search <query>")

                elif cmd == 'mode':
                    if arg:
                        self.change_mode(arg)
                    else:
                        print(f"Current mode: {self.engine.get_mode()}")
                        print("Usage: mode <hybrid|online|offline>")

                elif cmd == 'history':
                    self.show_history()

                elif cmd == 'offline-list':
                    self.list_offline_articles()

                elif cmd == 'clear':
                    self.engine.clear_cache()
                    print("✅ Cache cleared")

                elif cmd == 'help':
                    self.print_menu()

                else:
                    print(f"❌ Unknown command: {cmd}")
                    print("   Type 'help' for available commands")

            except KeyboardInterrupt:
                print("\n\n👋 Interrupted. Goodbye!")
                break
            except Exception as exc:  # pylint: disable=broad-except
                print(f"❌ Error: {exc}")


def main():
    """Main entry point for the CLI application."""
    cli = AIBOT_CLI()
    cli.run()


if __name__ == "__main__":
    main()
