from __future__ import annotations

import subprocess

import sublime
import sublime_plugin


class RestartInSafeModeCommand(sublime_plugin.ApplicationCommand):
    def run(self, *, restart: bool = True) -> None:
        if sublime.ok_cancel_dialog(
            "In order to restart in safe mode, the current Sublime Text has to be closed."
            + " Be careful, unsaved changes may lose. Are you sure to continue?"
        ):
            self.open_safe_mode(close_self=restart)

    @staticmethod
    def open_safe_mode(*, close_self: bool = True) -> None:
        if sublime.platform() == "windows":
            startupinfo = subprocess.STARTUPINFO()  # type: ignore
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW  # type: ignore
        else:
            startupinfo = None  # type: ignore

        subprocess.Popen([sublime.executable_path(), "--safe-mode"], shell=True, startupinfo=startupinfo)

        if close_self:
            sublime.run_command("exit")
