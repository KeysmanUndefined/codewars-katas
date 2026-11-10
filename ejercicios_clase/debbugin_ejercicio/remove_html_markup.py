def remove_html_markup(s):
    tag = False
    quote = False
    remove_html_markup = ""
    
    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
            
        elif (c == "'" or c == '"') and tag:
            quote = not quote
        elif not tag:
            remove_html_markup = remove_html_markup + c 
        else:
            pass    
            
    return remove_html_markup
            
if __name__ == "__main__":
            
       print(remove_html_markup("<b>foo</b>"))        
       print(remove_html_markup('"<b>foo</b>"'))       
       print(remove_html_markup('<b>"foo"</b>'))       
       print(remove_html_markup('<"b">foo</"b">'))
