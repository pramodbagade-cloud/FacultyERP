class WindowUtils:

    @staticmethod
    def center_and_fit(
        window,
        preferred_width=1500,
        preferred_height=850,
        min_width=1000,
        min_height=700,
        margin=40
    ):
        window.update_idletasks()

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        width = min(preferred_width, screen_width - margin)
        height = min(preferred_height, screen_height - margin)

        width = max(width, min_width)
        height = max(height, min_height)

        x = max((screen_width - width) // 2, 0)
        y = max((screen_height - height) // 2, 0)

        window.geometry(f"{width}x{height}+{x}+{y}")
        window.minsize(min_width, min_height)