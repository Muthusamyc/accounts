<!DOCTYPE html>
<html>
<head>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
            vertical-align: top;
        }
        .scrollable {
            max-height: 200px;
            overflow-y: auto;
            word-wrap: break-word;
        }
    </style>
</head>
<body>

<table>
    <tr>
        <th>Column 1</th>
        <th>Column 2</th>
    </tr>
    <tr>
        <td>Short text</td>
        <td class="scrollable">Long text goes here. Long text goes here. Long text goes here. Long text goes here. Long text goes here. Long text goes here. Long text goes here. Long text goes here. Long text goes here. Long text goes here.</td>
    </tr>
</table>

</body>
</html>
