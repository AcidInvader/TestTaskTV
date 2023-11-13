import React from 'react';


const CommentItem = ({comment}) => {
    return (
        <tr>
            <td>{comment.author.username}</td>
            <td>{comment.content}</td>
            <td>{comment.article}</td>
        </tr>
    )
}


const CommentList = ({comments}) => {

    return (
        <table>
            <tr>
                <th>Author Name</th>
                <th>Comment_text</th>
                <th>Article</th>
            </tr>
            {comments.map((comment) => <CommentItem comment={comment} />)}
        </table>
    )
}


export default CommentList