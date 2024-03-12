# requirement - Add table in UI to display messages
* i created a table using following functions,
* ( we should start and stop the function when we call a function)
* (eg : <>-start ,</>-stop)
    * TABLE 
    * TH 
    * TR
    * TD 
FUNCTIONS : 
### <TABLE>- TABLE
### <TR> - TABLE ROWS
### <TH> - TABLE HEADER
### <TD> - TABLE DATA 


* The data here to be print in different rows everytime when user gives input, for this i included below code in body of index.html


### note:
    * here i called a  {FOR LOOP  and
    * i called  (TR)  function in {FOR LOOP
    * and called  (TD)  function in (TR)
  
ex :
```html
 <table>
     <tr>
        <th>messages</th>
     </tr>
   {% for message in messages %}
      <tr>
           <td>{{ message[0] }}</td>
      </tr>
   {% endfor %}
 </table>
```