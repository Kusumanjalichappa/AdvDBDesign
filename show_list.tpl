<p><b>Basic Todo List Kusumanjali's Experimantal Version</b></p>
<hr/>
<table border="1">
%for row in rows:
    <tr>
    %for item in row[1:]:
        <td>{{item}}</td>
    %end
        <td>
            <a href="/delete_item/{{row[0]}}"> DELETE </a>
        </td>
    </tr>
%end
</table>
</br>
</br>
<a href="/new_item"><b> NEW ITEM </b></a>
<hr/>
