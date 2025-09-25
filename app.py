from flask import Flask, render_template, request, redirect, url_for, flash
from models import Supplier
from services import SupplierService

app = Flask(__name__)
app.secret_key = "dev-secret-key"

service = SupplierService()

@app.route("/")
def index():
    return redirect(url_for("list_suppliers"))

@app.route("/suppliers")
def list_suppliers():
    suppliers = service.list()
    return render_template("suppliers_list.html", suppliers=suppliers)

@app.route("/suppliers/new", methods=["GET", "POST"])
def new_supplier():
    if request.method == "POST":
        try:
            data = Supplier(
                name=request.form.get("name", "").strip(),
                address=request.form.get("address", "").strip(),
                email=request.form.get("email", "").strip(),
                phone=request.form.get("phone", "").strip(),
            )
            service.create(data)
            flash("Fournisseur ajouté avec succès.", "success")
            return redirect(url_for("list_suppliers"))
        except Exception as e:
            flash(f"Erreur de validation : {e}", "danger")
    default = Supplier(name="ElecTout",
                       address="6 Av de la République, 74 100 Cluses",
                       email="daniel.larieux@wanadoo.fr",
                       phone="00 33 06 25 15 86")
    return render_template("supplier_form.html", supplier=default, mode="create")

@app.route("/suppliers/<int:supplier_id>/edit", methods=["GET", "POST"])
def edit_supplier(supplier_id: int):
    s = service.get(supplier_id)
    if not s:
        flash("Fournisseur introuvable.", "warning")
        return redirect(url_for("list_suppliers"))
    if request.method == "POST":
        try:
            data = Supplier(
                name=request.form.get("name", "").strip(),
                address=request.form.get("address", "").strip(),
                email=request.form.get("email", "").strip(),
                phone=request.form.get("phone", "").strip(),
            )
            service.update(supplier_id, data)
            flash("Fournisseur modifié avec succès.", "success")
            return redirect(url_for("list_suppliers"))
        except Exception as e:
            flash(f"Erreur de validation : {e}", "danger")
    return render_template("supplier_form.html", supplier=s, mode="edit")

if __name__ == "__main__":
    app.run(debug=True)
