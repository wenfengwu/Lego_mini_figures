from flask import render_template, jsonify, request
from miniFig_app import app, cache
from miniFig_app.models.sell_fig import Sell_fig
from miniFig_app.models.figure import Figure
from miniFig_app.form import AddToCartForm
import math


all_themes = [
    "General", "Basic Set", "Disney Princess", "Duplo, Town", "Castle", "City", "Star Wars", "Harry Potter"
]


@app.route('/browse_fig')
def browse_all():
    return render_template('browse_all.html')

@app.route('/browse_fig/by_selection')
# @cache.cached(timeout=300, query_string=True)
def fetch_all():
    selection = request.args.get('selection', 'most_popular') # Get selection argument 
    page_number = request.args.get('page_number', '1') # Get selection page_number 
    if page_number.isdigit():
        page_number = int(page_number)
    else:
        page_number = 1
    page_limit = request.args.get('page_limit', '10') # Get selection page_limit
    if page_limit.isdigit():
        page_limit = int(page_limit)
    else:
        page_limit = 10

    offset = (page_number - 1) * page_limit # Calculate database offset
    """
    Pagination if page size = 10
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    10, 11, 12, 13, 14, 15, 16, 17, 18, 19
    """
    # query data and pass to the html
    if selection == 'on_sale':
        data = [data.figure for data in Sell_fig.get_all_sell_by_selection(offset=offset, page_size=page_limit)]
        total_pages = math.ceil(Sell_fig.count_all() * 1.0 / page_limit)
    else:
        data = Figure.browse_all(offset=offset, page_size=page_limit)
        total_pages = math.ceil(Figure.count_all() * 1.0 / page_limit)

    # Calculate page nubmer
    
    total_page_indicator = min(5, total_pages) # Only show 4 page indicators

    next_page = None
    prev_page = None
    if page_number > 1:
        prev_page = f"load_data(\"{selection}\", \"{page_number - 1}\", \"{page_limit}\")"
    if page_number + total_page_indicator <= total_pages:
        next_page = f"load_data(\"{selection}\", \"{page_number + total_page_indicator}\", \"{page_limit}\")"
    
    page_data = []
    for page_index in range(0, total_page_indicator):
        current_page = page_number + page_index
        on_click = f"load_data(\"{selection}\", \"{current_page}\", \"{page_limit}\")"
        page_data.append((current_page, on_click))

    return jsonify(
        {
            'html': render_template('by_all_sell.html', data=data),
            'pagination': render_template('pagination.html', prev_page=prev_page, next_page=next_page, page_data=page_data)
        }
    )


@app.route('/browse_fig/by_search')
@cache.cached(timeout=300, query_string=True)
def search_by_name():
    term = request.args.get('search', '')
    data = Figure.search_by_name(term)
    return jsonify({'html': render_template('by_search_term.html', data=data)})


@app.route('/browse_fig/year')
@cache.cached(timeout=300)
def browse_all_by_year():
    return render_template('year.html')


@app.route('/browse_fig/by_year/<year>')
def fetch_by_year(year=2021):
    # selection = request.args.get('selection') # Get selection argument 
    page_number = request.args.get('page_number', '1') # Get selection page_number 
    if page_number.isdigit():
        page_number = int(page_number)
    else:
        page_number = 1
    page_limit = request.args.get('page_limit', '10') # Get selection page_limit
    if page_limit.isdigit():
        page_limit = int(page_limit)
    else:
        page_limit = 10

    offset = (page_number - 1) * page_limit # Calculate database offset
  
    # query data and pass to the html
    data = Figure.browse_all_by_year(year, offset=offset, page_size=page_limit)
    
    # Calculate page nubmer
    total_pages = math.ceil(Figure.count_all() * 1.0 / page_limit)
    total_page_indicator = 4 # Only show 4 page indicators

    next_page = None
    prev_page = None
    if page_number > 1:
        prev_page = f"load_data(\"{year}\", \"{page_number - 1}\", \"{page_limit}\")"
    if page_number + total_page_indicator + 1 <= total_pages:
        next_page = f"load_data(\"{year}\", \"{page_number + total_page_indicator + 1}\", \"{page_limit}\")"
    
    page_data = []
    for page_index in range(page_number, page_number + total_page_indicator + 1):
        on_click = f"load_data(\"{year}\", \"{page_index}\", \"{page_limit}\")"
        page_data.append((page_index, on_click))

    return jsonify(
        {
            'html': render_template('by_year.html', data=data),
            'pagination': render_template('pagination.html', prev_page=prev_page, next_page=next_page, page_data=page_data)
        }
    )

@app.route('/browse_fig/theme')
@cache.cached(timeout=300)
def browse_all_by_theme():
    return render_template('theme.html',all_themes=all_themes)


@app.route('/browse_fig/by_theme/<theme>')
@cache.cached(timeout=300, query_string=True)
def fetch_by_theme(theme="General"):
    # selection = request.args.get('selection') # Get selection argument 
    page_number = request.args.get('page_number', '1') # Get selection page_number 
    if page_number.isdigit():
        page_number = int(page_number)
    else:
        page_number = 1
    page_limit = request.args.get('page_limit', '10') # Get selection page_limit
    if page_limit.isdigit():
        page_limit = int(page_limit)
    else:
        page_limit = 10

    offset = (page_number - 1) * page_limit # Calculate database offset

    # query data and pass to the html
    data = Figure.browse_all_by_theme(theme, offset=offset, page_size=page_limit)
    
    # Calculate page nubmer
    total_pages = math.ceil(Figure.count_all() * 1.0 / page_limit)
    total_page_indicator = 4 # Only show 4 page indicators

    next_page = None
    prev_page = None
    if page_number > 1:
        prev_page = f"load_data(\"{theme}\", \"{page_number - 1}\", \"{page_limit}\")"
    if page_number + total_page_indicator + 1 <= total_pages:
        next_page = f"load_data(\"{theme}\", \"{page_number + total_page_indicator + 1}\", \"{page_limit}\")"
    
    page_data = []
    for page_index in range(page_number, page_number + total_page_indicator + 1):
        on_click = f"load_data(\"{theme}\", \"{page_index}\", \"{page_limit}\")"
        page_data.append((page_index, on_click))

    return jsonify(
        {
            'html': render_template('by_theme.html', data=data),
            'pagination': render_template('pagination.html', prev_page=prev_page, next_page=next_page, page_data=page_data)
        }
    )
    


@app.route('/display_minifig/<id>')
@cache.cached(timeout=300, query_string=True)
def get_one_detailed_fig(id):
    form = AddToCartForm()
    detailed_fig = Figure.get_one_by_fig_id(id)
    sell_info = Sell_fig.get_all_sell_info_by_fig_id(id)
    blindbox = Sell_fig.get_blindbox()
    return render_template('display_minifig.html', detailed_fig=detailed_fig, sell_info=sell_info, form=form, blindbox=blindbox)


