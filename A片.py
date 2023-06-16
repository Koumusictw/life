import webbrowser
urL='https://youtube.com/shorts/iiZBUlwsLAo?feature=share'
chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new(urL)