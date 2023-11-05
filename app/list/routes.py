from app.list import bp
from flask import render_template
from app.extensions import db
from app.models.search_params import Search_param

@bp.route('/list')
def list_of_params():
    params_list = db.session.execute(db.select(Search_param)).scalars()
    return render_template('list_of_params.html',params_list=params_list)
 

@bp.route('/delete/<int:paramid>', methods=['DELETE'])
def delete_param(paramid):
    param_to_delete = db.get_or_404(Search_param,paramid)
    db.session.delete(param_to_delete)
    db.session.commit()
    return '', 204