const approveButtons = $(".approve-btn");
const deleteButtons = $(".delete-btn");

for (let button of approveButtons) {
    $(button).click( (e) => {
        let comment = e.target.dataset.target_comment;
        /**
         * Opens a new window to carry out the database update
         * to the comments approval status. The window automatically
         * gets closed in views.py when done, then location.reload
         * gets exectued to display the updated comment status and
         * retain the same scroll positon the user had.
         */
        const approveWindow = window.open(`approve_comment/${comment}`, "approve", "popup=1 width=100 height=100");
        const closedCheck = setInterval(() => {
            if (approveWindow.closed) {
              clearInterval(closedCheck);
              location.reload()
              alert('Comment Approved, window closed!');
            }
          }, 100);
    })
}