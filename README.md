# Site Generator
 a static site generator from scratch! A static site generator takes raw content files (like Markdown and images) 
 and turns them into a static website (a mix of HTML and CSS files).

 When converting, it will only support a single level of nesting when it comes to inline elements.
 This is supported:
 This is text with a **bolded phrase** in the middle
 
 This is NOT currently supported(Might add support for it later): 
 This is an *italic and **bold** word*.

## Installation
1. Download and use the converter.py to convert markdown to html. 

**BUT** If you run the main.py file in the console it gives you two options **1.** to use the converter to convert a file. **2.** To convert everything from the public folder to html and then open it on an offline server to see it as a webpage. This is not interactive at all and it is not meant to actually be good design or simulate "proper" behavior, but I wanted to preserve the original function of the program to show the code works with the files I have in the public directory. 

Also after running main.py it will use the files in public to open to open the local server  but after the first time you need to terminate the process for it to be able to be used again... I will fix that later so that it stops when closing the browser or the GUI. 

## Acknowledgements
This project was made possible thanks to the tutorials I followed at boot.dev 
   
