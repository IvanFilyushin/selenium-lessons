def test_basket(app):
    before = app.get_basket_size()
    for i in range(3):
        app.add_new_article()
    assert app.get_basket_size() == before + 3
    app.delete_articles()
    assert app.get_basket_size() == 0
