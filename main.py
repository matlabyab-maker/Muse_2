"""Muse_2: a small Kivy Android menu app starter."""
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex


BG = get_color_from_hex("#101722")
PANEL = get_color_from_hex("#1A2635")
ACCENT = get_color_from_hex("#49C5B6")
TEXT = get_color_from_hex("#F2F6FC")
MUTED = get_color_from_hex("#A9B8C9")


class MuseMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=dp(18), spacing=dp(12), **kwargs)
        self.status = Label(text="Ready", size_hint_y=None, height=dp(28), color=ACCENT,
                            halign="left", valign="middle")
        self.add_widget(Label(text="MUSE 2", font_size="30sp", bold=True,
                              color=TEXT, size_hint_y=None, height=dp(58)))
        self.add_widget(Label(text="A clean Android menu foundation", font_size="14sp",
                              color=MUTED, size_hint_y=None, height=dp(30)))

        self.entry = TextInput(hint_text="Write a note or message…", multiline=True,
                               size_hint_y=None, height=dp(110), padding=dp(12),
                               background_color=PANEL, foreground_color=TEXT,
                               hint_text_color=MUTED, cursor_color=ACCENT)
        self.add_widget(self.entry)

        scroll = ScrollView(do_scroll_x=False)
        buttons = BoxLayout(orientation="vertical", spacing=dp(9), size_hint_y=None)
        buttons.bind(minimum_height=buttons.setter("height"))
        actions = [
            ("Save note", self.save_note),
            ("Copy text", self.copy_text),
            ("Open website", self.open_website),
            ("About Muse_2", self.about),
            ("Clear", self.clear_text),
        ]
        for caption, callback in actions:
            button = Button(text=caption, size_hint_y=None, height=dp(48),
                            background_normal="", background_color=PANEL,
                            color=TEXT, font_size="16sp")
            button.bind(on_release=callback)
            buttons.add_widget(button)
        scroll.add_widget(buttons)
        self.add_widget(scroll)
        self.add_widget(self.status)

    def notify(self, message):
        self.status.text = message

    def save_note(self, *_):
        try:
            with open("muse_note.txt", "w", encoding="utf-8") as file:
                file.write(self.entry.text)
            self.notify("Note saved inside app storage")
        except OSError as error:
            self.notify(f"Save failed: {error}")

    def copy_text(self, *_):
        try:
            from kivy.core.clipboard import Clipboard
            Clipboard.copy(self.entry.text)
            self.notify("Text copied")
        except Exception:
            self.notify("Clipboard is unavailable")

    def open_website(self, *_):
        import webbrowser
        try:
            webbrowser.open("https://www.google.com")
            self.notify("Requested website open")
        except Exception:
            self.notify("Could not open website")

    def about(self, *_):
        self.notify("Muse_2 • Kivy • Android min API 24")

    def clear_text(self, *_):
        self.entry.text = ""
        self.notify("Text cleared")


class Muse2App(App):
    title = "Muse_2"

    def build(self):
        self.root_widget = MuseMenu()
        self.root_widget.canvas.before.clear()
        from kivy.graphics import Color, Rectangle
        with self.root_widget.canvas.before:
            Color(*BG)
            self.background = Rectangle(pos=self.root_widget.pos, size=self.root_widget.size)
        self.root_widget.bind(pos=self._update_bg, size=self._update_bg)
        return self.root_widget

    def _update_bg(self, widget, *_):
        self.background.pos = widget.pos
        self.background.size = widget.size


if __name__ == "__main__":
    Muse2App().run()
