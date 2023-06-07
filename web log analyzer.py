from logging import root
import tkinter as tk
from tkinter import filedialog
from collections import Counter
import re

def analyze_logs():
    # open file dialog to select log file
    filepath = filedialog.askopenfilename(filetypes=[("Log files", "*.log")])
    if not filepath:
        return
    
    #read log file and extract relevant information.
    with open(filepath, "r") as file:
        logs = file.readlines()
        
    #process log and analyze data
    # extraction the requested URLs and counting their occurrences.
    
    url_counter = Counter()
    for log in logs:
        match = re.search(r'"GET\s(.*?)\sHTTP', log)
        if match:
            url = match.group(1)
            url_counter[url] += 1
            
    #Display results in a new window.
    result_window = tk.Toplevel(root)
    result_window.title("Log Analysis Results")
    
    # Create a text widget to display the results.
    result_text = tk.Text(result_window)
    result_text.pack()
    
    #display the results.
    for url, count in url_counter.most_common():
        result_text.insert(tk.END, f"URL: {url}\tCount: {count}\n")
        
    #create the main tkinter window.
    root = tk.Tk()
    root.title("Web Server Log Analyzer")
    
    #create a button to open the log file and alayze it.
    analyze_button = tk.Button(root, text="Analyze Logs", command=analyze_logs)
    analyze_button.pack(pady=10)
    
    #start the tkinter event loop
    root.mainloop()
    