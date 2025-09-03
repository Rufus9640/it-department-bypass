#!/usr/bin/env python3
"""
Simple HTTP server for the Auto Page Refresh tool
Professional version for keeping sessions active
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.path = '/simple.html'
        return super().do_GET()

def main():
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    PORT = 8000
    
    while PORT < 8010:
        try:
            with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
                print(f"🚀 Auto Page Refresh server starting...")
                print(f"🌐 Server running at: http://localhost:{PORT}")
                print(f"📁 Serving files from: {script_dir}")
                print(f"🔄 Professional session keep-alive tool ready!")
                print(f"⏹️  Press Ctrl+C to stop the server")
                print("-" * 50)
                
                try:
                    webbrowser.open(f'http://localhost:{PORT}')
                    print(f"🎯 Browser should open automatically!")
                except:
                    print(f"💡 Manually open: http://localhost:{PORT}")
                
                httpd.serve_forever()
                
        except OSError:
            PORT += 1
            continue
        break
    else:
        print("❌ Could not find an available port between 8000-8009")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
        print("👋 Thanks for using Auto Page Refresh!")
