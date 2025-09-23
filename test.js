function ist() 
  { console.log("Run 1");};

function iind() {
    setTimeout(() => {
        console.log("Run 2, it will delay for 4 seconds");
    }, 4000);
}

function ithree() {
    console.log("Run 3");
}

ist();
iind();
ithree();

