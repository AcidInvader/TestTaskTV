import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios'
import {BrowserRouter, Route, Routes, Link, Navigate} from 'react-router-dom'
import ArticleList from './components/Articles.js'
import CommentList from './components/Comments.js'
import ArticleCommentList from './components/ArticleCommentsList.js'
import LoginForm from './components/Auth.js'
import Cookies from 'universal-cookie';


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'articles': [],
            'comments': [],
            'token': '',
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () =>this.load_data())
    }

    is_authenticated() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () =>this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8888/api/sign-in/', {username: username, password: password})
        .then(response => {
            this.set_token(response.data['token'])
        }).catch(error => alert('Password or Login is wrong'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
    if (this.is_authenticated())
        {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }


    load_data() {
        const headers = this.get_headers()
        axios
            .get('http://127.0.0.1:8888/api/articles/', {headers})
            .then(response => {
                const articles = response.data
                this.setState({
                    'articles': articles
                })
            }).catch(error => {
            console.log(error)
            this.setState({articles: []})
            })

        axios
            .get('http://127.0.0.1:8888/api/comments/', {headers})
            .then(response => {
                const comments = response.data
                this.setState({
                    'comments': comments
                })
            })
            .catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_from_storage()
    }


    render () {
        return (
            <div className="App">
                <BrowserRouter>
                <nav>
                    <ul>
                        <li>
                            <Link to='/'>Articles</Link>
                        </li>
                        <li>
                            {this.is_authenticated() ? <button
                            onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                        </li>
                    </ul>
                </nav>
                    <Routes>
                        <Route exact path='/' element = {<ArticleList articles={this.state.articles} />} />
                        <Route exact path='/articles' element = {<Navigate to='/' />} />
                        <Route exact path='/login' element = {<LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>} />
                        <Route exact path='/articles/:id' element = {<ArticleCommentList comments={this.state.comments} />} />
                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
