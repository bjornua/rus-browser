<%inherit file="/main.mako" />
<h1>
    ${escape(name)}
</h1>
<form action="${url_for("rus.save", id=id)}" method="post">
    <p>
        <label for="name">Navn</label>
        <br/>
        <input type="text" id="name" name="name" value=${esc_attr(name or "")} />
    </p>
    <p>
        <label for="phone">Telefon</label>
        <br/>
        <input type="text" id="phone" name="phone" value=${esc_attr(phone or "")} />
    </p>
    <p>
        <label for="email">Email</label>
        <br/>
        <input type="text" id="email" name="email" value=${esc_attr(email or "")} />
    </p>
    <p>
        <input type="submit" value="Gem" />
    </p>
</form>
