import tkinter as tk
from OreskossTCG.app import OreskossTCGApp

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = OreskossTCGApp(root)
        root.mainloop()
    except Exception as e:
        print(f"Error occurred: {e}")
        input("Press Enter to exit...")
