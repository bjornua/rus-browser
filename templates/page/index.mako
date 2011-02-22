<%inherit file="/main.mako" />
<h1>
    Doctag
</h1>

<h3>Upload document</h3>
<form action="${url_for("doc.upload")}" method="post" enctype="multipart/form-data">
    <p>
        Tags: <input type="text" name="tags" />
        File: <input type="file" name="document" />
    </p>
    <p>
        <input type="submit" value="Upload document" />
    </p>
</form>

<h3>Dokumenter</h3>
<form>
    Filter: <input type="text" />
</form>
<table>
    <thead>
        <tr>
            <th>Tags</th>
            <th>Thumbnail</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <span>Skat</span>
                <span>2007</span>
            </td>
        </tr>
    </tbody>

</table>
