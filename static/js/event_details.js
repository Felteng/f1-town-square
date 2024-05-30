const approveButtons = document.querySelectorAll(".approve-btn");
const deleteButtons = document.querySelectorAll(".delete-btn");


/**
 * Check if we need to restore the scroll position which will always
 * be the case if the user has clicked any of the CRUD buttons
 * after HttpResponseRedirect has ben executed in the view.
 * It will not be the case when the page is first loaded as there
 * won't be any scroll position captured, that happens when a button is clicked.
 * 
 * Clear the scrollPosition so that it won't be reused every time the page is loaded.
 */
const scrollPosition = localStorage.getItem('scrollPosition');
if (scrollPosition) {
  window.scrollTo(0, parseInt(scrollPosition));
  localStorage.removeItem('scrollPosition');
}


// Approve button functionality
approveButtons.forEach(button => {
  /**
   * Given the button clicked is linked to a valid comment id
   * store the current scroll position so that it can be
   * restored when the user is returned to the event page.
   * 
   * Redirect to approve_comment view where HttpResponseRedirect will be
   * executed after the comment approval has been attempted to return the user
   * to the previous page, ie the event page where the comment was made.
   */
  $(button).click((e) => {
    const commentId = e.target.dataset.target_comment;
    console.log(commentId)

    if (commentId) {
      // Store current scroll position
      localStorage.setItem('scrollPosition', window.scrollY);
      window.location.href = `approve_comment/${commentId}`;
    } else {
      console.error('Comment ID not found.');
    }
  });
});


// Delete button functionality
deleteButtons.forEach(button => {
    /**
   * Given the button clicked is linked to a valid comment id
   * store the current scroll position so that it can be
   * restored when the user is returned to the event page.
   * 
   * Redirect to delete_comment view where HttpResponseRedirect will be
   * executed after the comment deletion has been attempted to return the user
   * to the previous page, ie the event page where the comment was made.
   */
  $(button).click((e) => {
    const commentId = e.target.dataset.target_comment;
    console.log(commentId)

    if (commentId) {
      // Store current scroll position
      localStorage.setItem('scrollPosition', window.scrollY);
      window.location.href = `delete_comment/${commentId}`;
    } else {
      console.error('Comment ID not found.');
    }
  });
});