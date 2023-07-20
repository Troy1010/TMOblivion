// This variable is automatically set. I'm not sure if much of the statement is necessary
sampler2D TESR_RenderedBuffer : register(s0) = sampler_state { ADDRESSU = CLAMP; ADDRESSV = CLAMP; MAGFILTER = LINEAR; MINFILTER = LINEAR; MIPFILTER = LINEAR; };

// This variable allows data to be passed in from a CSE script. It seems using 4d variables here is standard for Oblivion Reloaded Shaders.
float4 TESR_TMLightingData; // x:Contrast value

// These structs seem standard for Oblivion Reloaded Shaders.
struct VSOUT
{
	float4 vertPos : POSITION;
	float2 UVCoord : TEXCOORD0;
};

struct VSIN
{
	float4 vertPos : POSITION0;
	float2 UVCoord : TEXCOORD0;
};

// This function is for the VertexShader. It seems standard for Oblivion Reloaded Shaders. Without it, the camera moves a little on activation, but I'm not sure if it causes other problems in its absence as well.
VSOUT FrameVS(VSIN IN)
{
	VSOUT OUT = (VSOUT)0.0f;
	OUT.vertPos = IN.vertPos;
	OUT.UVCoord = IN.UVCoord;
	return OUT;
}

// The main function for adjusting pixels
float4 TMShaderPass(VSOUT IN) : COLOR0
{
	float3 Color = tex2D(TESR_RenderedBuffer, IN.UVCoord).rgb;
	// Color = float3(min(max((Color.r - 128)*0.9f + 128,0),256),min(max((Color.g - 128)*0.9f + 128,0),256),min(max((Color.b - 128)*0.9f + 128,0),256));
	Color = float3((Color.r - 0.5f)*1.1f + 0.5f,(Color.g - 0.5f)*1.1f + 0.5f,(Color.b - 0.5f)*1.1f + 0.5f);
	// Color = float3(Color.x*0.5,Color.y*0.5,Color.z*0.5);
	// Color = float3(Color.r*0.5,Color.g*0.5,Color.b*0.5);
	// Color = float3(Color.r,Color.g,Color.b);
	// Color *= 0.5;
	return float4(Color, 1.0f);
}

technique
{
	pass
	{
		VertexShader = compile vs_3_0 FrameVS();
		PixelShader  = compile ps_3_0 TMShaderPass();
	}
}