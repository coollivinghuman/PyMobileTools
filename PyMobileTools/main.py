# start of the PROJECT yay

import customtkinter as ctk
import cmessage

cm = cmessage.CMessage()
cmmsg = cm.Message()

cmmsg.Show(
    "PyMobileTools Warning",
    "This is a small project. It may have bugs and errors. "
    "That doesn't mean that you don't have to use it.",
    None,
    cm.ICON_WARNING
)

cmmsg.Show(
    "Python may be required.",
    "As I said, this is a small project. Make sure that Python "
    "is in your PATH, otherwise this program may not work.",
    None,
    cm.ICON_WARNING
)


# -------------------------
# Downgrade Device window
# -------------------------

def open_downgrade():
    downgrade_window = ctk.CTkToplevel(root)

    downgrade_window.title("Downgrade Device")
    downgrade_window.geometry("500x300")
    downgrade_window.resizable(False, False)

    # Keep the window above the main window
    downgrade_window.transient(root)
    downgrade_window.lift()
    downgrade_window.focus_force()

    checking_label = ctk.CTkLabel(
        downgrade_window,
        text="Checking for Signed IPSW-s...",
        font=("Arial", 15)
    )

    checking_label.pack(pady=100)

    def show_versions():
        checking_label.configure(
            text="Signed IPSW-s:"
        )

        versions = [
            "iOS 26.6",
            "iOS 27 Beta 1",
            "iOS 27 Beta 2",
            "iOS 27 Beta 3",
            "iOS 27 Beta 4",
            "iOS 27 Beta 5"
        ]

        for version in versions:
            button = ctk.CTkButton(
                downgrade_window,
                text=version,
                width=250
            )

            button.pack(pady=4)

    # Demo: wait 5 seconds
    downgrade_window.after(5000, show_versions)


# -------------------------
# Main window
# -------------------------

root = ctk.CTk()

root.title("PyMobileTools")
root.geometry("800x500")
root.resizable(False, False)

# Downgrade Device button
downgrade_button = ctk.CTkButton(
    root,
    text="Downgrade Device",
    width=140,
    height=30,
    command=open_downgrade
)

downgrade_button.place(x=10, y=10)

# Version label
version_label = ctk.CTkLabel(
    root,
    text="PyMobileTools InDev. This is a demo!",
    text_color="black",
    fg_color="#90EE90",
    corner_radius=0
)

version_label.pack(
    side="bottom",
    fill="x"
)

root.mainloop()