import webbrowser
#for i in range(10):
urL='https://youtu.be/dQw4w9WgXcQ'
chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new(urL)