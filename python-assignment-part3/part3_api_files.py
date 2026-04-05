import requests
import datetime

print("Task 1 - File Read and Write")

# Write
notes = ["Topic 1: Variables store data. Python is dynamically typed.",
          "Topic 2: Lists are ordered and mutable.",
          "Topic 3: Dictionaries store key-value pairs.",
          "Topic 4: Loops automate repetitive tasks.",
          "Topic 5: Exception handling prevents crashes."
         ]

# opening the file in write mode
file = open("python_notes.txt", "w", encoding="utf-8")
for line in notes:
    file.write(line + "\n")
file.close()

print("File written successfully.")

# appending 2 more lines to the file
file =open("python_notes.txt", "a", encoding="utf-8")
file.write("Topic 6: Python supports OOP.\n")
file.write("Topic 7: The syntax is simple and readable.\n")
file.close()

print("Lines appended.")

# reading the file
file = open("python_notes.txt", "r", encoding="utf-8")
all_lines = file.readlines()
file.close()

# printing and counting the lines
print("\n File Contents:")
c = 1
for line in all_lines:
    print(f"{c}. {line.strip()}")
    c += 1

print("\n Total lines in the file:", len(all_lines))

# user input operation
word = input("\nEnter a word to search in the file: ")
found = False

for line in all_lines:
    if word.lower() in line.lower():
        print(f"'{word}' found in: {line.strip()}")
        found = True

if not found:
    print(f"Not found in the file.")


print("\n Task 2 - API Integration")

url = "https://dummyjson.com/products"

# fetch 20 products and show them in a table

resp = requests.get(url + "?limit=20")
product_list = resp.json()["products"]

print("\n All 20 products:")
print(f"\n{'ID':<5} | {'Title':<30} | {'Category':<20} | {'Price':>10} | {'Rating':}")
print("-" * 80)

for item in product_list:
    print(f"{item['id']:<5} | {item['title']:<30} | {item['category']:<20} | {item['price']:>10} | {item['rating']}")

# filter products with rating >= 4.5 and sort them by price in descending order

desired_products = []
for item in product_list:
    if item["rating"] >= 4.5:
        desired_products.append(item)

desired_products.sort(key=lambda x: x["price"], reverse=True)

print("\n Products with rating >= 4.5 sorted by price (desc):")
print(f"\n{'ID':<5} | {'Title':<30} | {'Category':<20} | {'Price':>10} | {'Rating':}")
print("-" * 80)

for item in desired_products:
    print(f"{item['id']:<5} | {item['title']:<30} | {item['category']:<20} | {item['price']:>10} | {item['rating']}")

# fetch all laptops from the laptops category

laptop_resp = requests.get(url + "/category/laptops")
laptop_list = laptop_resp.json()["products"]

print("\n All laptops:")
for laptop in laptop_list:
    print("Name:", laptop["title"], " | Price:", laptop["price"])

# send a POST request to add a new product

new_product = {
  "title": "My Custom Product",
  "price": 999,
  "category": "electronics",
  "description": "A product I created via API"
}

post_resp = requests.post(url + "/add", json=new_product)
result = post_resp.json()

print("\n POST request response:")
for k in result:
    print(f"{k}: {result[k]}")

print("\n Task 3 - Exception Handling")

# safe_divide function

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"
    except TypeError:
        return "Error: Both inputs must be numbers"

print("\n Testing safe_divide:")
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))

# Guarded file reader

def read_file_safe(filename):
    try:
        f = open(filename, "r", encoding="utf-8")
        content = f.read()
        f.close()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found")
    finally:
        print("File operation complete")

print("\n Testing read_file_safe:")
print(read_file_safe("python_notes.txt"))
print(read_file_safe("ghost_file.txt"))

# wrap API calls in try-except blocks

def fetch_products_safe(url):
    try:
        r = requests.get(url + "?limit=20")
        return r.json()["products"]
    except requests.exceptions.ConnectionError:
        print("Connection failed. Pls check your internet")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later")
    except Exception as e:
        print("Something went wrong:", e)
    return[]

def add_product_safe(product_data):
    try:
        r = requests.post(url + "/add", json=product_data)
        return r.json()
    except requests.exceptions.ConnectionError:
        print("Connection failed. Pls check your internet")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later")
    except Exception as e:
        print("Something went wrong:", e)
    return None

# loop to look up products by ID

print("\n Product lookup (enter ID 1-100 or type Quit to stop):")

while True:
    user_input = input("Enter product ID or 'quit': ").strip()

    if user_input.lower() == "quit":
        print("Stopped lookup")
        break

    # check if it is actually a number
    try:
        pid= int(user_input)
    except ValueError:
        print("That's not a number, Try again")
        continue

    # check range
    if pid < 1 or pid >100:
        print("Pls enter a no. b/w 1-100")
        continue

    # make the request
    try:
        r = requests.get(url + "/" + str(pid))
    except requests.exceptions.ConnectionError:
        print("Connection Failed, Pls check your internet")
        continue
    except requests.exceptions.Timeout:
        print("Request timed out. try again later")
        continue
    except Exception as e:
        print("Error:", e)
        continue

    if r.status_code == 404:
        print("Product not found")
    elif r.status_code == 200:
        p = r.json()
        print("Title:", p["title"])
        print("Price:$" + str(p["price"]))
    else:
        print("Got unexpected status:", r.status_code)



print("\n Task 4 - Logging to File")
log_file = "error_log.txt"

# function to write one error line to the log

def write_log(where, what_happened):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = "[" + now + "] ERROR in " + where + ":" + what_happened + "\n"
    f = open(log_file, "a", encoding="utf-8")
    f.write(line)
    f.close()

# intentionally trigger a ConnectionError through a fake URL

print("\nTrying an unreachable URL to trigger ConnectionError...")
try:
    requests.get("https://this-host-does-not-exist-xyz.com/api")
except requests.exceptions.ConnectionError:
    write_log("fetch_products", "Timeout - server took too long to respond")
    print("Timeout caught and saved to log")
except Exception as e:
    write_log("fetch_products", str(e))

# request a product ID that doesn't exist to get a 404
print("Requesting product ID 999 to trigger a 404...")
r2 = requests.get(url + "/999")

if r2.status_code != 200:
    write_log("lookup_product", "HTTPError - 404 Not Found for product ID 999")
    print("404 response logged")

print("\n Contents of error_log.txt:")
f= open(log_file, "r", encoding="utf-8")
print(f.read())
f.close()




    