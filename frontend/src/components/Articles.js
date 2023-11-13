import React from 'react'
import {Link} from 'react-router-dom'
import {useParams} from 'react-router-dom'
import {Table} from 'react-bootstrap'

const ArticleItem = ({article}) => {
    return (
        <tr>
            <td>{article.id}</td>
            <td>
                <Link to={`/articles/${article.id}`}>
                {article.title}
                </Link>
            </td>
            <td>
                {article.content}
            </td>
        </tr>
    )
}

const ArticleList = ({articles}) => {
    const articleItems = articles.map((article) => <ArticleItem article={article} />)
    console.log("articleItems...", articleItems[0])
    return (
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="row">Id</th>
                    <th scope="col">Title</th>
                    <th scope="col">Content</th>
                </tr>
            </thead>
            <tbody>{articleItems}</tbody>
        </table>
    )
}

export default ArticleList


