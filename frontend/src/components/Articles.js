import React from 'react'
import {Link} from 'react-router-dom'
import {useParams} from 'react-router-dom'

const ArticleItem = ({article}) => {
    return (
    <tr>
        <Link to={`/articles/${article.id}`}>
            <td>{article.id}</td>
            <td>{article.title}</td>
            <td>{article.content}</td>
        </Link>
    </tr>
    )
}


const ArticleList = ({articles}) => {
    return (
        <table>
            <th>
                Id
            </th>
            <th>
                Title
            </th>
            <th>
                Content
            </th>
            {articles.map((article) => <ArticleItem article={article} />)}
        </table>
    )
}

export default ArticleList


