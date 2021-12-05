from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required
from miniFig_app import app, db
from miniFig_app.form import PostSellFigForm, SellItemUpdateForm
from miniFig_app.models.sell_fig import Sell_fig


@app.route('/sell_fig', methods=['GET', 'POST'])
@login_required
def sell_fig():
    form = PostSellFigForm()
    if form.validate_on_submit():
        sell_fig = Sell_fig(quantity=form.fig_quantity.data, sell_price=form.fig_price.data,
                            figure_id=form.fig_id.data, user_id=int(current_user.get_id()))
        db.session.add(sell_fig)
        db.session.commit()
        return redirect(url_for('user_profile'))
    return render_template('sell_fig.html', title='Post to Sell', form=form)


@app.route('/sell_fig/delete/<id>')
@login_required
def delete_sell_fig(id):
    Sell_fig.delete_item(id)
    return redirect(url_for('user_profile'))


@app.route('/sell_fig/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit_sell_fig(id):
    form = SellItemUpdateForm()
    if form.validate_on_submit():
        Sell_fig.edit_item(form, id)
        return redirect(url_for('user_profile'))
    elif request.method == 'GET':
        item = Sell_fig.get_item(id)
        form.sell_price.data = item.sell_price
        form.quantity.data = item.quantity
    return render_template('sell_edit.html', title='Edit Sell Item', form=form)

