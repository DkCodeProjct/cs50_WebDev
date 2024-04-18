
document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);


  // By default, load the inbox

  load_mailbox('inbox');

  document.querySelector('#compose-form').addEventListener('submit',sendMail) // some call for loading func

});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#email-detail-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function emailView(id) {
  
  fetch(`/emails/${id}`)
    
  .then(res => res.json())
    .then(email => {
      console.log(email);

      document.querySelector('#emails-view').style.display = 'none';
      document.querySelector('#compose-view').style.display = 'none';
      document.querySelector('#mail-data').style.display = 'block';

      document.querySelector('#mail-data').innerHTML = `
      <ul class="list-group">
        <li class="list-group-item"><strong>From:</strong> ${email.sender}</li>
        <li class="list-group-item"><strong>To:</strong> ${email.recipients}</li>
        <li class="list-group-item"><strong>Subject:</strong> ${email.subject}</li>
        <li class="list-group-item"><strong>Timestamp:</strong> ${email.timestamp}</li>
        <li class="list-group-item">${email.body}</li>
      </ul>` // boostrp proprty[ul]

      if (!email.read) {
        
        fetch(`/emails/${email.id}`, {
          method: 'PUT',
          body: JSON.stringify({ read: true })
       
        });
      }

      const archBtn = document.createElement('button');
      archBtn.innerHTML = email.archived ? 'Unarchive' : 'Archive';
      
      archBtn.addEventListener('click', function() {
        
        fetch(`/emails/${email.id}`, {
          method: 'PUT',
          body: JSON.stringify({ archived: !email.archived })
        
        })
        
        /*.then(() => {
          load_mailbox('archive')
        })*/
        .then(() => {
          setTimeout(function(){ load_mailbox('archive') }, 1000);//delay loading ddb rec
         
        })
      
      });
      document.querySelector('#mail-data').append(archBtn);
     
      // reply functionality
      const replyBtn= document.createElement('button');
      
      replyBtn.textContent = 'Reply'
      replyBtn.addEventListener('click',()=> {
        compose_email();
        document.querySelector('#compose-recipients').value = email.sender;
        let sub = email.subject;
        if (sub.split(' ',1)[0] != 'reply:'){
          subject = 'reply'+email.subject; // getting first word n checkIfIt's='reply' else;reply//
        }
        document.querySelector('#compose-subject').value = '';
        document.querySelector('#compose-body').value = `on ${email.timestamp} ${email.seder} reply: ${email.body}`;// preFilling subject

      })
      document.querySelector('#mail-data').append(replyBtn);


    })
    .catch(error => console.error('Error:', error));
}



function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  
  
  fetch(`/emails/${mailbox}`) // dont put inside the fetch
    /*method:'GET',*/
    .then(res => res.json())
    .then(emails => {
      emails.forEach(mail=> {
        console.log(mail);

        const updateMail = document.createElement('div')
        /*updateMail.className = 'list-group-item';*/ // make box in mail{boostrp proprty}
        updateMail.className = 'list-group-item';
        updateMail.innerHTML = `<h6>sender:${mail.sender}</h6>,
          <h5>subject:${mail.subject}</h5>, 
          <p>date:${mail.timestamp}</p>`;   //timstamp from model.py;
        updateMail.className = mail.read ? 'read':'unRead';
        updateMail.addEventListener('click', function(){
          emailView(mail.id)
        });

      document.querySelector('#emails-view').append(updateMail)
    })
  
  });
  
};



// sent func

function sendMail(event){
  event.preventDefault() // prevent from load to inbox views[like this]

  const recipients = document.querySelector('#compose-recipients').value; // default id's=#....
  const subject = document.querySelector('#compose-subject').value;
  const body = document.querySelector('#compose-body').value;
  fetch('/emails', {
    method:'POST',
    body: JSON.stringify({
      recipients: recipients,
      subject:  subject,
      body: body,
    })
  })
  .then(res => res.json())
  .then(result => {
    console.log(result)
    
      load_mailbox('sent');
  }); // sent func done
}
