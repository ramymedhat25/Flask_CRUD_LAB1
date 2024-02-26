from flask import Flask,request,render_template,redirect,url_for

app=Flask(__name__)
users=[{"id":1,"name":"mina", 'age' : 30, 'location' : 'Giza'},{"id":2,"name":"ahmed", 'age' : 20, 'location' : 'Minia'},{"id":3,"name":"mariam", 'age' : 22, 'location' : 'Minia'},{"id":4,"name":"Ramy", 'age' : 26, 'location' : 'Benisuef'}]

def get_next_id():
  if len(users)>0:
    return users[-1]['id']+1
  else:
    return 1

@app.route('/')
def get_users():
  name=request.args.get("name")
  age=request.args.get("age")
  location=request.args.get("location")
  if(name!=None or age!=None or location !=None):
    users.append({'id':get_next_id(), 'name' : name , 'age' : age , 'location' : location})
  print(users)
  if users != []:
    return render_template('users.html', users_html =  users)
  else:
    return "<h1>No Users Found</h1>"



@app.route('/delete/<int:id>')
def delete_user(id):
  if id != None and len(users) != 0:
    for i  in range(len(users)):
      if users[i]['id'] == id:
        del users[i]
        print("Found and Delete")
        break
  return redirect('/')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    if request.method == 'POST':
        update_user(id)
        return redirect('/')
    else:
        user_to_edit = get_user_by_id(id)
        return render_template('edit_user.html', user=user_to_edit)


def update_user(id):
    name = request.form.get("name")
    age = request.form.get("age")
    location = request.form.get("location")
    
    if any([name, age, location]):
        for user in users:
            if user['id'] == id:
                user.update({'name': name, 'age': age, 'location': location})
                break


def get_user_by_id(id):
    for user in users:
        if user['id'] == id:
            return user
    return None




if __name__=="__main__":
  app.run(debug=True)