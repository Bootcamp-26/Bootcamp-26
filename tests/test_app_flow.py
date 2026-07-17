"""Lightweight UI smoke tests that do not require API keys or Ollama."""

import unittest

from streamlit.testing.v1 import AppTest


def _app() -> AppTest:
    return AppTest.from_file("app.py", default_timeout=20).run()


class AppFlowTests(unittest.TestCase):
    def test_welcome_screen_and_theme_switcher(self) -> None:
        app = _app()

        self.assertFalse(app.exception)
        self.assertEqual(app.session_state["step"], "theme_selection")
        self.assertEqual(app.text_input[0].placeholder, "Bugün neyin üzerine düşünmek istiyorsun?")

        app.button(key="messy_mode").click().run()
        self.assertFalse(app.exception)
        self.assertEqual(app.session_state["theme_mode"], "messy")

    def test_idea_cards_expand_without_external_services(self) -> None:
        app = _app()
        app.session_state["step"] = "idea_selection"
        app.session_state["theme"] = "Sürdürülebilir şehirler"
        app.session_state["generated_ideas"] = [
            "1. Sessiz Rota — Gürültü kirliliği düşük yürüyüş rotaları üretir.",
            "2. Döngü Haritası — Mahalle bazlı paylaşım ve geri dönüşüm ağı kurar.",
            "3. Gölge İzleri — Yaz aylarında serin ve gölgeli rotaları gösterir.",
        ]
        app.run()

        self.assertFalse(app.exception)
        app.button(key="idea_card_2").click().run()

        self.assertFalse(app.exception)
        self.assertTrue(app.session_state["active_idea"].startswith("2. Döngü Haritası"))
        self.assertEqual(app.button(key="research_2").label, "Bu fikri araştır  →")

    def test_chat_workspace_renders_sources_and_history(self) -> None:
        app = _app()
        app.session_state["step"] = "chat"
        app.session_state["selected_idea"] = "Döngü Haritası"
        app.session_state["research_sources"] = [
            {
                "title": "Circular Cities Guide",
                "url": "https://example.org/guide",
                "content": "Kentlerde döngüsel ekonomi için uygulama örnekleri.",
            }
        ]
        app.session_state["messages"] = [
            {"role": "user", "content": "Bu fikir kimin için?"},
            {"role": "assistant", "content": "Mahalle sakinleri ve yerel yönetimler için."},
        ]
        app.run()

        self.assertFalse(app.exception)
        self.assertEqual(app.expander[0].label, "Araştırma kaynakları · 1")
        self.assertEqual(len(app.chat_message), 2)
        self.assertEqual(app.chat_input[0].placeholder, "Fikrinle ilgili bir şey sor…")

if __name__ == "__main__":
    unittest.main()
