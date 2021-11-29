# GLSL

vertex_shader_toon = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;

out vec3 outColor;
out vec2 outTexCoords;

void main()
{
    vec4 norm = vec4(normal, 0.0);

    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;

    vec4 light = vec4(pointLight, 1.0);

    float intensity = dot(modelMatrix * norm, normalize(light - pos));


    gl_Position = projectionMatrix * viewMatrix * pos;

    outColor = vec3(1.0,1.0 - valor * 2,1.0-valor * 2) * intensity;
    outTexCoords = texCoords;
}
"""


fragment_shader_toon = """
#version 450
layout (location = 0) out vec4 fragColor;

in vec3 outColor;
in vec2 outTexCoords;

uniform sampler2D tex;

void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords);
}
"""
vertex_shader_inflado = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;

out vec3 outColor;
out vec2 outTexCoords;

void main()
{
    vec4 norm = vec4(normal, 0.0);

    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;

    vec4 light = vec4(pointLight, 1.0);

    float intensity = dot(modelMatrix * norm, normalize(light - pos));

    if (intensity > 0.8)
        intensity = 1;
    else if (intensity > 0.6)
        intensity = 0.8;
    else if (intensity > 0.3)
        intensity = 0.6;
    else intensity = 0;

    gl_Position = projectionMatrix * viewMatrix * pos;

    outColor = vec3(1.0,1.0 - valor * 2,1.0-valor * 2) * intensity;
    outTexCoords = texCoords;
}
"""

fragment_shader_inflado = """
#version 450
layout (location = 0) out vec4 fragColor;

in vec3 outColor;
in vec2 outTexCoords;

uniform sampler2D tex;

void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords);
}
"""


vertex_shader_tiempo = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;

out vec3 outColor;
out vec2 outTexCoords;

void main()
{
    vec4 norm = vec4(normal, 0.0);

    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;

    vec4 light = vec4(pointLight, 1.0) * tiempo;

    float intensity = dot(modelMatrix * norm, normalize(light - pos));

    if (intensity > 0.8)
        intensity = 1;
    else if (intensity > 0.6)
        intensity = 0.8;
    else if (intensity > 0.3)
        intensity = 0.6;
    else intensity = 0;

    gl_Position = projectionMatrix * viewMatrix * pos;

    outColor = vec3(1.0,1.0 - valor * 2,1.0-valor * 2) * intensity;
    outTexCoords = texCoords;
}
"""

fragment_shader_tiempo = """
#version 450
layout (location = 0) out vec4 fragColor;

in vec3 outColor;
in vec2 outTexCoords;

uniform sampler2D tex;

void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords);
}
"""

vertex_shader_color = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;

out vec3 outColor;
out vec2 outTexCoords;

void main()
{
    vec4 norm = vec4(normal, 0.0);

    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;

    vec4 light = vec4(pointLight, 1.0);

    float intensity = dot(modelMatrix * norm, normalize(light - pos));
    vec3 color = vec3(0, 0, 0);

    if (intensity > 0.8)
    {
        intensity = 1;
        color = vec3(1, 0, 0);
    }
    else if (intensity > 0.6)
    {
        intensity = 0.8;
        color = vec3(0, 1, 0);
    }
    else if (intensity > 0.3)
    {
        intensity = 0.6;
        color = vec3(0, 0, 1);
    }
    else intensity = 0;

    gl_Position = projectionMatrix * viewMatrix * pos;

    outColor = color * intensity;
    outTexCoords = texCoords;
}
"""

fragment_shader_color = """
#version 450
layout (location = 0) out vec4 fragColor;

in vec3 outColor;
in vec2 outTexCoords;

uniform sampler2D tex;

void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords);
}
"""