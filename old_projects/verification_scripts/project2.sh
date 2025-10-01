urls=(
    https://ww0xthb64c.execute-api.us-west-2.amazonaws.com/prod/
    https://edjtplfid6.execute-api.us-west-2.amazonaws.com/prod/
    https://2x3r1slz6d.execute-api.us-west-2.amazonaws.com/prod/
    https://mqebsjip30.execute-api.us-west-2.amazonaws.com/prod/
    https://ki4zd69n34.execute-api.us-west-2.amazonaws.com/prod/
    https://kp8a9g2b5m.execute-api.us-west-2.amazonaws.com/prod/
    https://dlkgboal0e.execute-api.us-west-2.amazonaws.com/prod/
    https://v9xb9ybix7.execute-api.us-west-2.amazonaws.com/prod/
    https://cxiqq3jdr3.execute-api.us-west-2.amazonaws.com/prod/
    https://0nc8stqe8j.execute-api.us-west-2.amazonaws.com/prod/
    https://mj1d1xz5gh.execute-api.us-west-2.amazonaws.com/prod/
    https://79hcwjlm00.execute-api.us-west-2.amazonaws.com/prod/
    https://wti1llpyjb.execute-api.us-west-2.amazonaws.com/prod/
    https://tl24bu3414.execute-api.us-west-2.amazonaws.com/prod/
    https://p2dsrjk44b.execute-api.us-west-2.amazonaws.com/prod/
    https://caddb7zla7.execute-api.us-west-2.amazonaws.com/prod/
    https://phjetn7h6a.execute-api.us-west-2.amazonaws.com/prod/
    https://hfx71vjyvl.execute-api.us-west-2.amazonaws.com/prod/
    https://4xmc5sewt4.execute-api.us-west-2.amazonaws.com/prod/
    https://l6bmiksx5d.execute-api.us-west-2.amazonaws.com/prod/
    https://vmgha66pp1.execute-api.us-west-2.amazonaws.com/prod/
    https://9ksc2qh8ni.execute-api.us-west-2.amazonaws.com/prod/
    https://0bnaj764df.execute-api.us-west-2.amazonaws.com/prod/
    https://fyxic8g92i.execute-api.us-west-2.amazonaws.com/prod/
    https://tfyc6z83a6.execute-api.us-west-2.amazonaws.com/prod/
    https://z1xn8v01tg.execute-api.us-west-2.amazonaws.com/prod/
    https://3b4bcwdo9j.execute-api.us-west-2.amazonaws.com/prod/
    https://3436bzjxz8.execute-api.us-west-2.amazonaws.com/prod/
    https://yx1tjnupza.execute-api.us-west-2.amazonaws.com/prod/
    https://19qzorpm52.execute-api.us-west-2.amazonaws.com/prod/
    https://lrpjoecf70.execute-api.us-west-2.amazonaws.com/prod/
    https://ipaue0h4a7.execute-api.us-west-2.amazonaws.com/prod/
    https://n0zn4w6n38.execute-api.us-west-2.amazonaws.com/prod/
    https://qko6gslila.execute-api.us-west-2.amazonaws.com/prod/
    https://016eg9deid.execute-api.us-west-2.amazonaws.com/prod/
)

echo "Number of URLs: ${#urls[@]}"

for url in "${urls[@]}"; do
    echo "$url"
    docker run -it --rm cs291_scripts ./project1.py "$url"

    # Wait for user input to continut
    read -p "Press enter to continue"
done