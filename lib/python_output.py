import inspect
from sys import settrace
import copy
import sys
import re


f = 0
current_variables = {}
tab = 0
inWhileLoop = False
inForLoop = False
whileloopID = []
forloopID = []
indent = 0
indentFor = 0
slideShowId = 0
# local trace function which returns itself


def my_tracer(frame, event, arg=None):
    global tab
    global current_variables
    global inWhileLoop
    global whileloopID
    global inForLoop
    global forloopID
    global indent
    global slideShowId
    global indentFor
    # extracts frame code
    code = frame.f_code

    # extracts calling function name
    func_name = code.co_name
    if func_name == 'encode' or func_name == 'main' or func_name[0] == "<":
        return

    # extracts the line number
    line_no = frame.f_lineno

    if event == 'call':
        prev_function = getattr(inspect.stack()[2],"function")
        call_entry = prev_function + " " + event + "ed " + func_name + " with arguments"
        for j, k in frame.f_locals.items():
            call_entry += "<br>" + str(j) + " -> " + str(k)
        print('''
		<button onclick="myFunction('Demo%s')" class="w3-btn w3-block w3-green w3-left-align">%s</button>
    	<div id="Demo%s" class="w3-container w3-hide" style="margin-left:10px;border-left-style:solid;border-left-width:10px;border-left-color: rgba(0, 128, 0, 0.3);">
		''' % (tab, call_entry, tab))

        tab += 1
    if event == 'return':
        call_exit = "function " + func_name + " " + event + "ed " + str(arg)
        print('''
		</div>
		<p>%s</p>
		''' % (call_exit))

    if event == 'line':
        new_variables = inspect.stack()[1][0].f_locals
        regex1 = r"(\s*)while.*"
        regex2 = r"(\s*)for.*"
        curr_code = getattr(inspect.stack()[1],"code_context")[0]
        match1 = re.search(regex1, curr_code)
        match2 = re.search(regex2, curr_code)

        for var in new_variables:
            if var not in current_variables:
                print("<div style=\"display:inline-block;width:50px;\"></div>", "<div style=\"display:inline-block;\">%s</div>" % (var + " = " + str(new_variables[var]) + " is introduced."),"<br>")

            else:
                if new_variables[var] != current_variables[var]:
                    print("<div style=\"display:inline-block;width:50px;\"></div>", "<div style=\"display:inline-block;\">%s</div>" % (var + " = " + str(current_variables[var]) + " -> " + str(new_variables[var])),"<br>")


        curr_indent = 0
        for c in curr_code:
            if c == " ":
                curr_indent+=1
            else:
                break

        if len(whileloopID)>0 and curr_indent < whileloopID[-1][1]+4:
            print("</div>")

        if len(forloopID)>0 and curr_indent < forloopID[-1][1]+4:
            print("</div>")

        if inWhileLoop and curr_indent < whileloopID[-1][1]+4 and whileloopID[-1][:2]!=[line_no,indent]:
            inWhileLoop = False
            print("""<a class="prev" onclick="plusSlides(-1,%s)">&#10094;</a>
<a class="next" onclick="plusSlides(1,%s)">&#10095;</a>
</div>""" % (whileloopID[-1][2], whileloopID[-1][2]))

            whileloopID.pop()

        if match1 != None:
            inWhileLoop = True
            indent = 0
            for c in curr_code:
                if c == " ":
                    indent+=1
                else:
                    break
            if len(whileloopID)==0 or whileloopID[-1][:2]!=[line_no,indent]:
                whileloopID.append([line_no,indent,slideShowId])
                print("<div id = \"ss%s\" class=\"slideshow-container\">" % (slideShowId))
                slideShowId+=1
            print("<div id=\"ms%s\" class=\"mySlides\">" % (whileloopID[-1][2]))

        if inForLoop and curr_indent < forloopID[-1][1]+4 and forloopID[-1][:2]!=[line_no,indentFor]:
            inForLoop = False
            print("""<a class="prev" onclick="plusSlides(-1,%s)">&#10094;</a>
<a class="next" onclick="plusSlides(1,%s)">&#10095;</a>
</div>""" % (forloopID[-1][2], forloopID[-1][2]))

            forloopID.pop()

        if match2 != None:
            inForLoop = True
            indentFor = 0
            for c in curr_code:
                if c == " ":
                    indentFor+=1
                else:
                    break
            if len(forloopID)==0 or forloopID[-1][:2]!=[line_no,indentFor]:
                forloopID.append([line_no,indentFor,slideShowId])
                print("<div id = \"ss%s\" class=\"slideshow-container\">" % (slideShowId))
                slideShowId+=1
            print("<div id=\"ms%s\" class=\"mySlides\">" % (forloopID[-1][2]))

        print("<div style=\"display:inline-block;width:50px;color:teal\">%s</div>" % (str(line_no-232)), "<div style=\"display:inline-block;\">%s</div>" % (curr_code),"<br>")
        current_variables = copy.deepcopy(new_variables)

    return my_tracer


def htmlInit():
    f = open("html_new1.html", 'w')
    sys.stdout = f
    print('''
		<!DOCTYPE html>
		<html>
		<title>ICSE DEMO 2021</title>
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <style>
        .slideshow-container {
            position: relative;
            background: rgba(0, 128, 0, 0.1);;
            }

            /* Slides */
            .mySlides {
            display: none;
            margin:5px;
            padding: 30px;
            padding-top: 10px;
            padding-bottom: 10px;
            }

            /* Next & previous buttons */
            .prev, .next {
            cursor: pointer;
            position: absolute;
            top: 50%;
            width: auto;
            margin-top: -20px;
            padding: 5px;
            color: rgba(0, 128, 0, 0.8);
            font-weight: bold;
            font-size: 20px;
            border-radius: 0 3px 3px 0;
            user-select: none;
            }

            /* Position the "next button" to the right */
            .next {
            position: absolute;
            right: 0;
            border-radius: 3px 0 0 3px;
            }

            /* On hover, add a black background color with a little bit see-through */
            .prev:hover, .next:hover {
            color: white;
            }

            /* The dot/bullet/indicator container */
            .dot-container {
            text-align: center;
            padding: 20px;
            background: #ddd;
            }

            /* The dots/bullets/indicators */
            .dot {
            cursor: pointer;
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #bbb;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
            }

            /* Add a background color to the active dot/circle */
            .active, .dot:hover {
            background-color: #717171;
            }

            /* Add an italic font style to all quotes */
            q {font-style: italic;}

            /* Add a blue color to the author */
            .author {color: cornflowerblue;}
        </style>
		<body>
		<div class="w3-container">

		<h2>Example</h2>
		<p>Open and collapse the accordian to see the summary</p>
	''')


htmlInit()

settrace(my_tracer)

def quick_sort(collection: list) -> list:
    if len(collection) < 2:
        return collection
    pivot = collection.pop()
    greater = []
    lesser = []
    for element in collection:
        (greater if element > pivot else lesser).append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    user_input = "32,13,56,24,87,5,44,42".strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(quick_sort(unsorted))


print('''<script>
var ss_count = %s;
function myFunction(id) {
  var x = document.getElementById(id);
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else {
    x.className = x.className.replace(" w3-show", "");
  }
}
var slideIndex = new Array(ss_count).fill(1);
var ind = 1;
for(ind = 0; ind < ss_count; ind++){
    showSlides(slideIndex[ind],ind);
}


function plusSlides(n,i) {
  showSlides(slideIndex[i] += n,i);
}

function currentSlide(n,i) {
  showSlides(slideIndex[i] = n,i);
}

function showSlides(n,i) {
  var k;
  var slides = document.getElementById("ss"+i).querySelectorAll('#ms'+i);
  console.log(slides)
  if (n > slides.length) {slideIndex[i] = 1}
    if (n < 1) {slideIndex[i] = slides.length}
    for (k = 0; k < slides.length; k++) {
      slides[k].style.display = "none";
    }
  slides[slideIndex[i]-1].style.display = "block";
}
</script>
</body>
</html>''' % (slideShowId))
