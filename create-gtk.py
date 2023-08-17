import os
import sys


if len(sys.argv) > 1:
    glade = sys.argv[1]
else:
    glade = "glad-0"

file = """
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyApp:
    def __init__(self):
        # Charger l'interface Glade
        builder = Gtk.Builder()
        builder.add_from_file("{0}.glade")

        # Lier les widgets avec les objets Python
        self.window = builder.get_object("main")
        self.label = builder.get_object("prenom")

        # Connecter les signaux aux méthodes
        builder.connect_signals(self)

    def on_valider_clicked(self, widget):
        self.label.set_label("Bonjour, Glade avec Python !")

    def on_window_destroy(self, widget):
        Gtk.main_quit()

if __name__ == "__main__":
    app = MyApp()
    app.window.show_all()
    Gtk.main()

""".format(
    glade
)

with open(glade + ".py", "w") as f:
    f.write(file)
