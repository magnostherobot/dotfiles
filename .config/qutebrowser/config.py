import subprocess
from os.path import expanduser

homepage = expanduser("~/.bg/qutebrowser-bindings.png")

c.hints.chars = "qwertyuiopasdfghjklzxcvbnm"
c.editor.command = ['urxvt', '-e', 'vim', '{}']
c.url.default_page = homepage
c.url.start_pages = homepage
c.url.searchengines = {
        "DEFAULT": "https://duckduckgo.com/?q={}",
        "g": "https://www.google.co.uk/search?q={}"
        }

# thing to read colourscheme from .Xresources:
def read_xresources(prefix):
    props = {}
    x = subprocess.run(
            ['xrdb', '-query'],
            stdout = subprocess.PIPE
            )
    lines = x.stdout.decode().split('\n')
    for line in filter(
            lambda l : l.startswith(prefix),
            lines
            ):
        prop, _, value = line.partition(':\t')
        props[prop] = value
    return props

xresources = read_xresources('*')
palette = {
        'base03': xresources['*color8'],
        'base02': xresources['*color0'],
        'base01': xresources['*color10'],
        'base00': xresources['*color11'],
        'base0': xresources['*color12'],
        'base1': xresources['*color14'],
        'base2': xresources['*color7'],
        'base3': xresources['*color15'],
        'yellow': xresources['*color3'],
        'orange': xresources['*color9'],
        'red': xresources['*color1'],
        'magenta': xresources['*color5'],
        'violet': xresources['*color13'],
        'blue': xresources['*color4'],
        'cyan': xresources['*color6'],
        'green': xresources['*color2']
        }

c.colors.completion.category.bg = palette['base03']
c.colors.completion.category.border.bottom = palette['base03']
c.colors.completion.category.border.top = palette['base03']
c.colors.completion.category.fg = palette['base3']
c.colors.completion.even.bg = palette['base02']
c.colors.completion.fg = palette['base1']
c.colors.completion.item.selected.bg = palette['violet']
c.colors.completion.item.selected.border.bottom = palette['violet']
c.colors.completion.item.selected.border.top = palette['violet']
c.colors.completion.item.selected.fg = palette['base3']
c.colors.completion.match.fg = palette['base2']
c.colors.completion.odd.bg = palette['base02']
c.colors.completion.scrollbar.bg = palette['base1']
c.colors.completion.scrollbar.fg = palette['base2']
c.colors.downloads.bar.bg = palette['base03']
c.colors.downloads.error.bg = palette['red']
c.colors.downloads.error.fg = palette['base3']
c.colors.downloads.start.fg = palette['base3']
c.colors.hints.bg = palette['violet']
c.colors.hints.fg = palette['base3']
c.colors.hints.match.fg = palette['base1']
c.colors.keyhint.fg = palette['base3']
c.colors.keyhint.suffix.fg = palette['yellow']
c.colors.messages.error.bg = palette['red']
c.colors.messages.error.border = palette['red']
c.colors.messages.error.fg = palette['base3']
c.colors.messages.info.bg = palette['base03']
c.colors.messages.info.border = palette['base03']
c.colors.messages.info.fg = palette['base3']
c.colors.messages.warning.bg = palette['orange']
c.colors.messages.warning.border = palette['orange']
c.colors.messages.warning.fg = palette['base3']
c.colors.prompts.bg = palette['base02']
c.colors.prompts.border = '1px solid ' + palette['base3']
c.colors.prompts.fg = palette['base3']
c.colors.prompts.selected.bg = palette['base01']
c.colors.statusbar.caret.bg = palette['blue']
c.colors.statusbar.caret.fg = palette['base1']
c.colors.statusbar.caret.selection.bg = palette['violet']
c.colors.statusbar.caret.selection.fg = palette['base1']
c.colors.statusbar.command.bg = palette['base03']
c.colors.statusbar.command.fg = palette['base1']
c.colors.statusbar.command.private.bg = palette['base01']
c.colors.statusbar.command.private.fg = palette['base3']
c.colors.statusbar.insert.bg = palette['base02']
c.colors.statusbar.insert.fg = palette['base1']
c.colors.statusbar.normal.bg = palette['base03']
c.colors.statusbar.normal.fg = palette['base1']
# c.colors.statusbar.passthrough.bg = palette['base02']
# c.colors.statusbar.passthrough.fg = palette['base1']
c.colors.statusbar.private.bg = palette['base01']
c.colors.statusbar.private.fg = palette['base3']
c.colors.statusbar.progress.bg = palette['base1']
c.colors.statusbar.url.error.fg = palette['red']
c.colors.statusbar.url.fg = palette['base1']
c.colors.statusbar.url.hover.fg = palette['base2']
c.colors.statusbar.url.success.http.fg = palette['base1']
c.colors.statusbar.url.success.https.fg = palette['base1']
c.colors.statusbar.url.warn.fg = palette['yellow']
# c.colors.tabs.bar.bg
c.colors.tabs.even.bg = palette['base02']
c.colors.tabs.odd.bg = palette['base1']
c.colors.tabs.indicator.error = palette['red']
c.colors.tabs.indicator.start = palette['violet']
c.colors.tabs.indicator.stop = palette['orange']
c.colors.tabs.odd.bg = palette['base03']
c.colors.tabs.odd.fg = palette['base1']
c.colors.tabs.selected.even.bg = palette['violet']
c.colors.tabs.selected.even.fg = palette['base2']
c.colors.tabs.selected.odd.bg = palette['violet']
c.colors.tabs.selected.odd.fg = palette['base2']
# c.colors.webpage.bg

# thing to set user stylesheets:
home = expanduser("~")

c.content.user_stylesheets = [
        ]
