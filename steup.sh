mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"victoriareworld@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml

echo "\
password=propm0000\n\
" > ~/.streamlit/secrets.toml
