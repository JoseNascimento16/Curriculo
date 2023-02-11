// export default function Header(){
function Header(){
    return(
        <header>
            <nav className="nav">
                <div className="left-header">
                    <img className="nav-logo" src="/static/img/react-logo.png" alt=""></img>
                    <h2>ReactFacts</h2>
                </div>
                <ul className="nav-items">
                    <li>Pricing</li>
                    <li>About</li>
                    <li>Contact</li>
                </ul>
            </nav>
        </header>
    )
}