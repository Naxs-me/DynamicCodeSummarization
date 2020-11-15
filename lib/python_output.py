# program to display the functioning of
# settrace()
import inspect
from sys import settrace
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
    # print(code)

    # extracts calling function name
    func_name = code.co_name
    if func_name == 'encode' or func_name == 'main' or func_name[0] == "<":
        return

    # extracts the line number
    line_no = frame.f_lineno
    # caller = frame.f_back
    # print(caller)
    # print(f"A {event} encountered in {func_name}() at line number {line_no} ")
    if event == 'call':
        # if func_name[0] == "<":
        #     func_name = func_name[1:-1]
        prev_function = getattr(inspect.stack()[2],"function")
        call_entry = prev_function + " " + event + "ed " + func_name + " with arguments"
        for j, k in frame.f_locals.items():
            call_entry += "<br>" + str(j) + " -> " + str(k)
        print('''
		<button onclick="myFunction('Demo%s')" class="w3-btn w3-block w3-black w3-left-align">%s</button>
    	<div id="Demo%s" class="w3-container w3-hide">
		''' % (tab, call_entry, tab))
        if func_name == "merge_sort":
            print('''<p>Description: <br>Pure implementation of the merge sort algorithm in Python<br>
			:param collection: some mutable ordered collection with heterogeneous comparable items inside<br>
			:return: the same collection ordered by ascending</p>''')
        if func_name == 'merge':
            print('''<p>Description: <br>merge left and right<br>
        :param left: left collection<br>
        :param right: right collection<br>
        :return: merge result<p>''')

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
                # print("temp",current_variables)
                print("&emsp;",var,"=",new_variables[var],"is introduced <br>")
            else:
                if new_variables[var] != current_variables[var]:
                    print("&emsp;",var,"=",current_variables[var],"->",new_variables[var],"<br>")

        curr_indent = 0
        for c in curr_code:
            if c == " ":
                curr_indent+=1
            else:
                break

        # if inWhileLoop and curr_indent >= whileloopID[-1][1]+4:
            # print("inside loop")
        if len(whileloopID)>0 and curr_indent < whileloopID[-1][1]+4:
            print("</div>")

        if len(forloopID)>0 and curr_indent < forloopID[-1][1]+4:
            print("</div>")


        # if whileloopID[-1][:2]==[line_no,indent]:
        #     print("<div class=\"mySlides\">")
        # else:



            # print("matched",match.group(0),indent,"</br>")
        if inWhileLoop and curr_indent < whileloopID[-1][1]+4 and whileloopID[-1][:2]!=[line_no,indent]:
            inWhileLoop = False
            print("""<a class="prev" onclick="plusSlides(-1,%s)">&#10094;</a>
<a class="next" onclick="plusSlides(1,%s)">&#10095;</a>
</div>""" % (whileloopID[-1][2], whileloopID[-1][2]))

            # print("exit loop")
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
                # print("first encounter")
                print("<div id = \"ss%s\" class=\"slideshow-container\">" % (slideShowId))
                slideShowId+=1
            # print(whileloopID)
            print("<div class=\"mySlides\">")
            # print("enter loop")

        if inForLoop and curr_indent < forloopID[-1][1]+4 and forloopID[-1][:2]!=[line_no,indentFor]:
            inForLoop = False
            print("""<a class="prev" onclick="plusSlides(-1,%s)">&#10094;</a>
<a class="next" onclick="plusSlides(1,%s)">&#10095;</a>
</div>""" % (forloopID[-1][2], forloopID[-1][2]))

            # print("exit loop")
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
                # print("first encounter")
                print("<div id = \"ss%s\" class=\"slideshow-container\">" % (slideShowId))
                slideShowId+=1
            # print(whileloopID)
            print("<div class=\"mySlides\">")
            # print("enter loop")



        # print("old",current_variables)
        print(str(line_no), curr_code ,"<br>")
        current_variables = new_variables.copy()
        # print("new",current_variables)
        # print(event + ' ' + str(code.co_names) + " line no " + str(line_no))



    return my_tracer


settrace(my_tracer)





def calc_profit(profit: list, weight: list, max_weight: int) -> int:
    """
    Function description is as follows-
    :param profit: Take a list of profits
    :param weight: Take a list of weight if bags corresponding to the profits
    :param max_weight: Maximum weight that could be carried
    :return: Maximum expected gain
    >>> calc_profit([1, 2, 3], [3, 4, 5], 15)
    6
    >>> calc_profit([10, 9 , 8], [3 ,4 , 5], 25)
    27
    """
    if len(profit) != len(weight):
        raise ValueError("The length of profit and weight must be same.")
    if max_weight <= 0:
        raise ValueError("max_weight must greater than zero.")
    if any(p < 0 for p in profit):
        raise ValueError("Profit can not be negative.")
    if any(w < 0 for w in weight):
        raise ValueError("Weight can not be negative.")

    # List created to store profit gained for the 1kg in case of each weight
    # respectively.  Calculate and append profit/weight for each element.
    profit_by_weight = [p / w for p, w in zip(profit, weight)]

    # Creating a copy of the list and sorting profit/weight in ascending order
    sorted_profit_by_weight = sorted(profit_by_weight)

    # declaring useful variables
    length = len(sorted_profit_by_weight)
    limit = 0
    gain = 0
    i = 0

    # loop till the total weight do not reach max limit e.g. 15 kg and till i<length
    while limit <= max_weight and i < length:
        # flag value for encountered greatest element in sorted_profit_by_weight
        biggest_profit_by_weight = sorted_profit_by_weight[length - i - 1]
        """
        Calculate the index of the biggest_profit_by_weight in profit_by_weight list.
        This will give the index of the first encountered element which is same as of
        biggest_profit_by_weight.  There may be one or more values same as that of
        biggest_profit_by_weight but index always encounter the very first element
        only.  To curb this alter the values in profit_by_weight once they are used
        here it is done to -1 because neither profit nor weight can be in negative.
        """
        index = profit_by_weight.index(biggest_profit_by_weight)
        profit_by_weight[index] = -1

        # check if the weight encountered is less than the total weight
        # encountered before.
        if max_weight - limit >= weight[index]:
            limit += weight[index]
            # Adding profit gained for the given weight 1 ===
            # weight[index]/weight[index]
            gain += 1 * profit[index]
        else:
            # Since the weight encountered is greater than limit, therefore take the
            # required number of remaining kgs and calculate profit for it.
            # weight remaining / weight[index]
            gain += (max_weight - limit) / weight[index] * profit[index]
            break
        i += 1
    return gain


def main():
        # l = [[4,2,5,6,10,15,4,8,3],[0, 5, 3, 2, 2],[-2, -5, -45]]

        # for i in l:
        # 	print("<p>For input " + str(i) + "</p>")
        # 	temp = merge_sort([4,2,5,6,10,15,4,8,3])
        # 	print("<p>Output is " + str(temp) + "</p><hr style=\"height:2px;border-width:0;color:gray;background-color:gray\">")

    profit = [int(x) for x in "5 8 7 1 12 3 4".split()]
    weight = [int(x) for x in "2 7 1 6 4 2 5".split()]
    max_weight = 100

    # Function Call
    calc_profit(profit, weight, max_weight)


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
            background: #f1f1f1f1;
            }

            /* Slides */
            .mySlides {
            display: none;
            padding: 80px;
            }

            /* Next & previous buttons */
            .prev, .next {
            cursor: pointer;
            position: absolute;
            top: 50%;
            width: auto;
            margin-top: -30px;
            padding: 16px;
            color: #888;
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
            background-color: rgba(0,0,0,0.8);
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
main()
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
var slideIndex = 1;
var ind = 0;
for(ind = 0; ind < ss_count; ind++){
    showSlides(slideIndex,ind);
}


function plusSlides(n,i) {
  showSlides(slideIndex += n,i);
}

function currentSlide(n,i) {
  showSlides(slideIndex = n,i);
}

function showSlides(n,i) {
  var i;
  var slides = document.getElementById("ss"+i).getElementsByClassName("mySlides");
  if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }
  slides[slideIndex-1].style.display = "block";
}
</script>
</body>
</html>''' % (slideShowId))


# returns reference to local
# trace function (my_tracer)
