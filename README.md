# Basic-A.I-Project-

When there's a snap or any noise picked up by the microphone, it will activate.

If it doesn't respond to a command, you'll be asked to manually type the command, and you can also issue commands by typing.

Here's a more advanced version of that sentence:

You can open and search anything using your default browser, but you'll need to set your default path. I had Edge, so I set it to Edge, but you can set your own default browser here:
            elif "search on edge" in query:
                try:
                    speak("What should I search?")
                    print("What should I search?")
                    search = take_command() 
                    print(f"Opening new tab with search query: {search}")
                    
                    encoded_search = urllib.parse.quote(search)
                    
                    search_url = f"https://www.bing.com/search?q={encoded_search}"
                    
                    edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                    wb.register('edge', None, wb.BackgroundBrowser(edge_path))
                    wb.get('edge').open_new_tab(search_url)
                    
                    print("Search query opened successfully.")
                except Exception as e:
                    print("Error opening search query:", e)
                    speak("Can't open now, please try again later.")
                    print("Can't open now, please try again later.")
