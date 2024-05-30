const approveButtons = document.querySelectorAll(".approve-btn");
const deleteButtons = document.querySelectorAll(".delete-btn");
    

// Check if we need to restore the scroll position
const scrollPosition = localStorage.getItem('scrollPosition');
console.log(scrollPosition)
if (scrollPosition) {
  window.scrollTo(0, parseInt(scrollPosition));
  localStorage.removeItem('scrollPosition');
}


// Approve button functionality
approveButtons.forEach(button => {
  $(button).click( (e) => {
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
