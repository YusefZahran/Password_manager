from account import Account

# General
PROGRAM_NAME = "Password Manager"
registered_users = {
    "h": "h"
}
user_accounts: list[Account] = []

# Passwords
SALT_DIRECTORY = "./salt/"
"""Salts directory for specifying where to store user salts"""

# UI
# General
PROGRAM_BACKGROUND_COLOR = "#2E3440"
LABEL_FOREGROUND_COLOR = "#FFFFFF"
BUTTON_BG_COLOR = "#313338"
ENTRY_BG_COLOR = "#313338"
FRAME_HIGHLIGHT_COLOR = "#485365"
SMALL_BUTTON_SIZE = 7
LARGE_BUTTON_SIZE = 10
DEFAULT_FONT = ('calibre', 10, 'normal')

# Main Menu
ROOT_WIDGET_WIDTH = 600
ROOT_WIDGET_HEIGHT = 400
