async function optimize() {

    const width =
        document.getElementById("width").value;

    const height =
        document.getElementById("height").value;

    const routers =
        document.getElementById("routers").value;

    const radius =
        document.getElementById("radius").value;

    const algorithm =
        document.getElementById("algorithm").value;

    const response = await fetch(
        "/optimize",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                width,
                height,
                routers,
                radius,
                algorithm
            })
        }
    );

    const data =
        await response.json();

    document.getElementById(
        "coverage"
    ).innerHTML =
        data.score + "%";

    document.getElementById(
        "executionTime"
    ).innerHTML =
        data.time + " s";

    document.getElementById(
        "algoName"
    ).innerHTML =
        data.algorithm;

    let routerHTML = "";

    data.routers.forEach(
        (router,index)=>{

            routerHTML += `
                <li>
                    Router ${index+1}
                    :
                    (${router[0]}, ${router[1]})
                </li>
            `;

        }
    );

    document.getElementById(
        "routerList"
    ).innerHTML =
        routerHTML;

    drawRouters(
        data.routers,
        radius
    );

}


async function compareAlgorithms(){

    const width =
        document.getElementById("width").value;

    const height =
        document.getElementById("height").value;

    const routers =
        document.getElementById("routers").value;

    const radius =
        document.getElementById("radius").value;

    const response = await fetch(
        "/compare",
        {
            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                width,
                height,
                routers,
                radius
            })
        }
    );

    const data =
        await response.json();

    let html = "";

    data.forEach(item=>{

        html += `
        <tr>
            <td>${item.name}</td>
            <td>${item.score}%</td>
            <td>${item.time}s</td>
        </tr>
        `;

    });

    document.getElementById(
        "comparisonBody"
    ).innerHTML =
        html;

}


function drawRouters(
    routers,
    radius
){

    const canvas =
        document.getElementById(
            "wifiCanvas"
        );

    const ctx =
        canvas.getContext("2d");

    ctx.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );

    const scale = 25;

    routers.forEach(router=>{

        const x =
            router[0] * scale;

        const y =
            router[1] * scale;

        // Coverage Area
        ctx.beginPath();

        ctx.arc(
            x,
            y,
            radius * scale,
            0,
            Math.PI * 2
        );

        ctx.fillStyle =
            "rgba(13,110,253,0.15)";

        ctx.fill();

        ctx.strokeStyle =
            "rgba(13,110,253,0.4)";

        ctx.stroke();

        // Router Point
        ctx.beginPath();

        ctx.arc(
            x,
            y,
            8,
            0,
            Math.PI * 2
        );

        ctx.fillStyle =
            "#0d6efd";

        ctx.fill();

    });

}