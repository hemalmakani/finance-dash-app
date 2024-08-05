import dash
import dash_bootstrap_components as dbc
from sqlalchemy import create_engine
import os

DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)



# Navigation bar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("HTS", href="/"))
        
    ],
    brand="Whats Working",
    brand_href="/",
    color="primary",
    dark=True,
)

# App layout
app.layout = dbc.Container([
    navbar,
    dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug=True)
