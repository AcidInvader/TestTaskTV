import React from 'react';
import {useParams} from 'react-router-dom'



const CommentItem = ({comment}) => {
    return (
        <tr>
            <td>{comment.author.username}</td>
            <td>{comment.content}</td>
            <td>{comment.article}</td>
        </tr>
    )
}


const ArticleCommentList = ({comments}) => {
    var {id} = useParams()
    console.log('comment', comments.article)
    var filteredComments = comments.filter((comment) => comment.article === parseInt(id))

    return (
        <table>
            <tr>
                <th>Author Name</th>
                <th>Comment_text</th>
                <th>Article</th>
            </tr>
            {filteredComments.map((comment) => <CommentItem comment={comment} />)}
        </table>
    )
}


export default ArticleCommentList