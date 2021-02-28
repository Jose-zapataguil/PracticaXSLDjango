<?xml version="1.0"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" version="5.0" encoding="UTF-8" indent="yes"/>
    <xsl:template match="/">
        <xsl:for-each select="Products/Product">
            <div class="col-lg-4 col-sm-6">
                <div class="single_category_product">
                    <div class="single_category_img">
                        <img>
                            <xsl:attribute name="src">
                                <xsl:text>pages/static/img/</xsl:text>
                                <xsl:value-of select="Imagen"/>
                            </xsl:attribute>
                            <xsl:attribute name="alt">
                                <xsl:value-of select="Thumbnail_URL"/>
                            </xsl:attribute>
                        </img>
                        <div class="category_social_icon">
                            <ul>
                                <li>
                                    <a href="#">
                                        <i class="ti-heart"></i>
                                    </a>
                                </li>
                                <li>
                                    <a href="#">
                                        <i class="ti-bag"></i>
                                    </a>
                                </li>
                            </ul>
                        </div>
                        <div class="category_product_text">
                            <xsl:attribute name="id">
                                <xsl:value-of select="Product_ID"/>
                            </xsl:attribute>
                            <a>
                                <xsl:attribute name="href">
                                    <xsl:value-of select="Product_URL"/>
                                </xsl:attribute>
                                <h5>
                                    <xsl:value-of select="Name"/>
                                </h5>
                            </a>
                            <p>
                                <xsl:value-of select="Retail_Price"/>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </xsl:for-each>

    </xsl:template>
</xsl:stylesheet>
