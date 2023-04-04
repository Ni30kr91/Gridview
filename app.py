from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

fees = {
    'Admission': 500,
    'Tuition': 1000,
    'Transport': 700,
    'Lab': 1000,
    'Computer': 700,
    'Music': 300
}

@app.route('/fees', methods=['GET', 'POST'])
def index():
    total = []
    if request.method == 'POST':
        checked_fees = request.form.getlist('fee')
        for fee in checked_fees:
            total = sum(fees[fee])
        total_amount = ' + '.join(checked_fees) + '+'.join(str(fees[fee]) for fee in checked_fees)
        return jsonify({'total': total, 'total_amount': total_amount})
    return render_template('table.html',)

if __name__ == '__main__':
    app.run(debug=True)