<%inherit file="/main.mako" />
<h1>
    RUS-Browser
</h1>
<p>
%if page > 0:
    <a href="${url_for("index", page=page-1)}">Forrige side</a>
%else:
    Forrige side
%endif
%if page < pagecount - 1:
    | <a href="${url_for("index", page=page+1)}">Næste side</a>
%else:
    | Næste side
%endif
</p>
<p>
%for x in range(pagecount):
%if x == page:
    [${unicode(x)}]
%else:
    <a href="${url_for("index", page=x)}">[${unicode(x)}]</a>
%endif
%endfor
</p>
<table>
    <thead>
        <tr>
            <th>Navn</th>
            <th>Telefon</th>
            <th>Adresse</th>
        </tr>
    </thead>
    <tbody>
%for (name,phone,email) in russer:
        <tr>
            <td>
                ${escape(name or "")}
            </td>
            <td>
                ${escape(phone or "")}
            </td>
            <td>
                ${escape(email or "")}
            </td>
        </tr>
%endfor
    </tbody>
</table>
