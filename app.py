from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Home Page route
@app.route("/")
def home():
    return render_template("home.html")

# Route to form used to add a new stock item
@app.route("/enternew")
def enternew():
    return render_template("stock.html")

# Route to add a new record (INSERT) stock item data to the database
@app.route("/addrec", methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            product = request.form['product']
            category = request.form['category']
            quantity = request.form['quantity']
            price = request.form['price']

            with sqlite3.connect('pharmacy_inventory.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Stock (Product, Category, Quantity, Price) VALUES (?, ?, ?, ?)", 
                            (product, category, quantity, price))

                con.commit()
                msg = "Record successfully added to database"
        except Exception as e:
            con.rollback()
            msg = f"Error in insert operation: {e}"

        finally:
            con.close()
            return render_template('result.html', msg=msg)

# Route to SELECT all data from the database and display in a table
@app.route('/list')
def list():
    con = sqlite3.connect("pharmacy_inventory.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT rowid, * FROM Stock")
    rows = cur.fetchall()
    con.close()
    return render_template("list.html", rows=rows)

# The routes for edit, editrec, and delete will need to reference the 'Stock' table 
# and the appropriate columns. Make sure to adapt your HTML forms to match the schema as well.

# Route that will SELECT a specific row in the database then load an Edit form 
@app.route("/edit", methods=['POST','GET'])
def edit():
    if request.method == 'POST':
        try:
            # Use the hidden input value of id from the form to get the rowid
            id = request.form['id']
            # Connect to the database and SELECT a specific rowid
            con = sqlite3.connect("pharmacy_inventory.db")
            con.row_factory = sqlite3.Row

            cur = con.cursor()
            cur.execute("SELECT rowid, * FROM Stock WHERE rowid = " + id)

            rows = cur.fetchall()
        except:
            id=None
        finally:
            con.close()
            # Send the specific record of data to edit.html
            return render_template("edit.html",rows=rows)

# Route used to execute the UPDATE statement on a specific record in the database
@app.route("/editrec", methods=['POST', 'GET'])
def editrec():
    if request.method == 'POST':
        try:
            # Retrieve the row ID and the updated stock item information from the form
            rowid = request.form['rowid']
            product = request.form['product']
            category = request.form['category']
            quantity = request.form['quantity']
            price = request.form['price']

            # Connect to the pharmacy inventory database and update the stock item
            with sqlite3.connect('pharmacy_inventory.db') as con:
                cur = con.cursor()
                # Use placeholders to avoid SQL injection
                cur.execute("UPDATE Stock SET Product=?, Category=?, Quantity=?, Price=? WHERE rowid=?", 
                            (product, category, quantity, price, rowid))

                con.commit()
                msg = "Record successfully updated in the database"
        except Exception as e:
            con.rollback()
            msg = f"Error in the update operation: {e}"

        finally:
            con.close()
            # Send the transaction message to result.html
            return render_template('result.html', msg=msg)

# Route used to DELETE a specific record in the database    
@app.route("/delete", methods=['POST'])
def delete():
    if request.method == 'POST':
        try:
            # Retrieve the row ID from the form
            rowid = request.form['id']
            # Connect to the database and DELETE a specific record based on rowid
            with sqlite3.connect('pharmacy_inventory.db') as con:
                cur = con.cursor()
                # Use a placeholder to prevent SQL injection
                cur.execute("DELETE FROM Stock WHERE rowid=?", (rowid,))

                con.commit()
                msg = "Record successfully deleted from the database"
        except Exception as e:
            con.rollback()
            msg = f"Error in the DELETE operation: {e}"

        finally:
            con.close()
            return render_template('result.html', msg=msg)


if __name__ == "__main__":
    app.run(debug=True)

