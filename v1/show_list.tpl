<p><b>Basic Todo List Kusumanjali's Experimantal Version</b></p>
<hr/>
<table border="1">
%for row in rows:
    <tr>
        <td>{{row[0]}}</td>
        <td><a href="/update_item/{{row[0]}}">{{row[1]}}</a>
        </td>
        <td>
        %if row[2]==0:
            <a href="/set_status/{{row[0]}}/1">{{row[2]}}</a>
        %else:
            <a href="/set_status/{{row[0]}}/0">{{row[2]}}</a>
        %end
        </td>
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
